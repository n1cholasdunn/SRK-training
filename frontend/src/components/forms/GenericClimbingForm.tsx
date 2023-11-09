import {useState} from 'react';
import {useForm} from 'react-hook-form';
import {
  ClimbingAssessmentFormSchema,
  ClimbingAssessmentFormValues,
} from '../../types/assessments/climbing';
import {zodResolver} from '@hookform/resolvers/zod';
import {useSubmitAssessment} from '../../hooks/useSubmitAssessment';

import PowerEnduranceAssessment from '../assessments/PowerEnduranceAssessment';
import MaxPullupsAssessment from '../assessments/MaxPullupsAssessment';
import MaxLockoffAssessment from '../assessments/MaxLockoffAssessment';
import FingerStrengthAssessment from '../assessments/FingerStrengthAssessment';
import OAFingerStrengthAssessment from '../assessments/OAFingerStrengthAssessment';
import OAPinchAssessment from '../assessments/OAPinchAssessment';

const assessmentConfig = {
  power_endurance: {
    component: PowerEnduranceAssessment,
    displayName: 'Power Endurance',
    route: 'assessments/climbing/power-endurance/',
  },
  max_pullups: {
    component: MaxPullupsAssessment,
    displayName: 'Max Pullups',
    route: 'assessments/climbing/max-pullups/',
  },
  max_lockoff: {
    component: MaxLockoffAssessment,
    displayName: 'Max Lockoff',
    route: 'assessments/climbing/max-lockoff/',
  },
  finger_strength: {
    component: FingerStrengthAssessment,
    displayName: 'Finger Strength',
    route: 'assessments/climbing/finger-strength/',
  },
  oa_finger_strength: {
    component: OAFingerStrengthAssessment,
    displayName: 'OA Finger Strength',
    route: 'assessments/climbing/oa-finger-strength/',
  },
  oa_pinch_strength: {
    component: OAPinchAssessment,
    displayName: 'OA Pinch Strength',
    route: 'assessments/climbing/oa-pinch-strength/',
  },
};

type AssessmentKey = keyof typeof assessmentConfig;

const GenericClimbingForm = () => {
  const [currentAssessmentKey, setCurrentAssessmentKey] =
    useState<AssessmentKey | null>(null);

  const {
    handleSubmit,
    register,
    control,
    formState: {errors},
  } = useForm<ClimbingAssessmentFormValues>({
    resolver: zodResolver(ClimbingAssessmentFormSchema),
  });

  const {mutate: submitClimbing} =
    useSubmitAssessment<ClimbingAssessmentFormValues>(
      currentAssessmentKey
        ? assessmentConfig[currentAssessmentKey]?.route
        : 'assessments/core/create/',
      ClimbingAssessmentFormSchema
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

  const onSubmit = (data: ClimbingAssessmentFormValues) => {
    console.log(data);

    submitClimbing(data);
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

export default GenericClimbingForm;
