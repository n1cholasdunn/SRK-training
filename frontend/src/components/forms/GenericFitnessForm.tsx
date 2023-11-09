import {useState} from 'react';
import HealthMarkersAssessment from '../assessments/HealthMarkersAssessment';
import MeasurementsAssessment from '../assessments/MeasurementsAssessment';
import {useForm} from 'react-hook-form';
import {
  FitnessAssessmentFormSchema,
  FitnessAssessmentFormValues,
} from '../../types/assessments/fitness';
import {zodResolver} from '@hookform/resolvers/zod';
import {useSubmitAssessment} from '../../hooks/useSubmitAssessment';
import YMCAStepAssessment from '../assessments/YMCAStepAssessment';
import OverheadSquatAssessment from '../assessments/OverheadSquatAssessment';
import PushUpAssessment from '../assessments/PushUpAssessment';
import SitReachAssessment from '../assessments/SitReachAssessment';
import DaviesAssessment from '../assessments/DaviesAssessment';
import SharkSkillsAssessment from '../assessments/SharkSkillsAssessment';
import CoreAssessment from '../assessments/CoreAssessment';

const assessmentConfig = {
  health_markers: {
    component: HealthMarkersAssessment,
    displayName: 'Health Markers',
    route: 'assessments/fitness/health-markers/',
  },
  measurements: {
    component: MeasurementsAssessment,
    displayName: 'Measurements',
    route: 'assessments/fitness/measurements/',
  },
  overhead_squat: {
    component: OverheadSquatAssessment,
    displayName: 'Overhead Squat',
    route: 'assessments/fitness/overhead-squat/',
  },
  ymca_step: {
    component: YMCAStepAssessment,
    displayName: 'YMCA Step',
    route: 'assessments/fitness/ymca-step/',
  },
  sit_reach: {
    component: SitReachAssessment,
    displayName: 'Sit and Reach',
    route: 'assessments/fitness/sit-reach/',
  },
  pushup: {
    component: PushUpAssessment,
    displayName: 'Pushup',
    route: 'assessments/fitness/pushup/',
  },
  davies: {
    component: DaviesAssessment,
    displayName: 'Davies',
    route: 'assessments/fitness/davies/',
  },
  shark_skills: {
    component: SharkSkillsAssessment,
    displayName: 'Shark Skills',
    route: 'assessments/fitness/shark-skills/',
  },
  core: {
    component: CoreAssessment,
    displayName: 'Core',
    route: 'assessments/fitness/core/',
  },
};

type AssessmentKey = keyof typeof assessmentConfig;
const GenericFitnessForm = () => {
  const [currentAssessmentKey, setCurrentAssessmentKey] =
    useState<AssessmentKey | null>(null);

  const {
    handleSubmit,
    register,
    control,
    formState: {errors},
  } = useForm<FitnessAssessmentFormValues>({
    resolver: zodResolver(FitnessAssessmentFormSchema),
  });

  const {mutate: submitFitness} =
    useSubmitAssessment<FitnessAssessmentFormValues>(
      currentAssessmentKey
        ? assessmentConfig[currentAssessmentKey]?.route
        : 'assessments/core/create/',
      FitnessAssessmentFormSchema
    );

  const renderAssessmentComponent = () => {
    if (currentAssessmentKey && assessmentConfig[currentAssessmentKey]) {
      const AssessmentComponent =
        assessmentConfig[currentAssessmentKey].component;
      return (
        <AssessmentComponent
          control={control}
          register={register}
          errors={errors}
        />
      );
    }
    return <div>Select an assesment to fill out</div>;
  };

  const onSubmit = (data: FitnessAssessmentFormValues) => {
    console.log(data);

    submitFitness(data);
  };
  const handleSelectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setCurrentAssessmentKey(e.target.value as AssessmentKey);
  };
  return (
    <div className="space-y-4">
      <div className="flex flex-col space-y-2">
        <label htmlFor="assessment-select">Select an assessment:</label>
        <select
          id="assessment-select"
          onChange={handleSelectChange}
          value={currentAssessmentKey || ''}
          className="border border-gray-300 rounded-md p-2">
          <option value="">Select an assessment</option>
          {Object.entries(assessmentConfig).map(([key, value]) => (
            <option key={key} value={key}>
              {value.displayName}
            </option>
          ))}
        </select>

        <form
          onSubmit={handleSubmit(onSubmit)}
          className="flex flex-col space-y-2">
          {currentAssessmentKey && assessmentConfig[currentAssessmentKey] ? (
            renderAssessmentComponent()
          ) : (
            <div>Select an assessment to fill out</div>
          )}

          <button type="submit">Submit Assessment</button>
        </form>
      </div>
    </div>
  );
};

export default GenericFitnessForm;
