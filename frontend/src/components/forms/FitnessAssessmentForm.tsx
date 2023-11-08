import {useForm} from 'react-hook-form';
import {zodResolver} from '@hookform/resolvers/zod';
import {
  FitnessAssessmentFormSchema,
  FitnessAssessmentFormValues,
} from '../../types/assessments/fitness';
import HealthMarkersAssessment from '../assessments/HealthMarkersAssessment';
import MeasurementsAssessment from '../assessments/MeasurementsAssessment';
import OverheadSquatAssessment from '../assessments/OverheadSquatAssessment';
import YMCAStepAssessment from '../assessments/YMCAStepAssessment';
import SitReachAssessment from '../assessments/SitReachAssessment';
import PushUpAssessment from '../assessments/PushUpAssessment';
import DaviesAssessment from '../assessments/DaviesAssessment';
import CoreAssessment from '../assessments/CoreAssessment';
import SharkSkillsAssessment from '../assessments/SharkSkillsAssessment';
import {useSubmitAssessment} from '../../hooks/useSubmitAssessment';

const FitnessAssessmentForm = () => {
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
      'assessments/fitness/testing/create/',
      FitnessAssessmentFormSchema
    );

  const onSubmit = (data: FitnessAssessmentFormValues) => {
    submitFitness(data);
  };

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className=" flex flex-col space-y-2">
      <h2>Health Markers Assessment</h2>
      <HealthMarkersAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>Measurements Assessment</h2>
      <MeasurementsAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>Overhead Squat Assessment</h2>
      <OverheadSquatAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>YMCA Step Assessment</h2>
      <YMCAStepAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>Sit and Reach Assessment</h2>
      <SitReachAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>Pushup Assessment</h2>
      <PushUpAssessment control={control} register={register} errors={errors} />
      <h2>Davies Assessment</h2>
      <DaviesAssessment control={control} register={register} errors={errors} />
      <h2>Shark Skills Assessment</h2>
      <SharkSkillsAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>Core Assessment</h2>
      <CoreAssessment control={control} register={register} errors={errors} />

      <button type="submit">Submit Assessments</button>
    </form>
  );
};

export default FitnessAssessmentForm;
