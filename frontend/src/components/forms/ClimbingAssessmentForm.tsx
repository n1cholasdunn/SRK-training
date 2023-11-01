import {zodResolver} from '@hookform/resolvers/zod';
import {
  AssessmentFormSchema,
  AssessmentFormValues,
} from '../../types/assessments/climbing';
import {useForm} from 'react-hook-form';
import PowerEnduranceAssessment from '../assessments/PowerEnduranceAssessment';
import MaxPullupsAssessment from '../assessments/MaxPullupsAssessment';
import MaxLockoffAssessment from '../assessments/MaxLockoffAssessment';
import FingerStrengthAssessment from '../assessments/FingerStrengthAssessment';
import OAFingerStrengthAssessment from '../assessments/OAFingerStrengthAssessment';
import OAPinchAssessment from '../assessments/OAPinchAssessment';

const ClimbingAssessmentForm = () => {
  const {
    handleSubmit,
    register,
    control,
    formState: {errors},
  } = useForm<AssessmentFormValues>({
    resolver: zodResolver(AssessmentFormSchema),
  });

  const onSubmit = (data: AssessmentFormValues) => {
    console.log(data);
  };

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className=" flex flex-col space-y-2">
      <h2>Power Endurance Assessment</h2>
      <PowerEnduranceAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>Max Pullups Assessment</h2>
      <MaxPullupsAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>Max Lockoff Assessment</h2>
      <MaxLockoffAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>Finger Strength Assessment</h2>
      <FingerStrengthAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>One Arm Finger Strength Assessment</h2>
      <OAFingerStrengthAssessment
        control={control}
        register={register}
        errors={errors}
      />
      <h2>One Arm Pinch Strength Assessment</h2>
      <OAPinchAssessment
        control={control}
        register={register}
        errors={errors}
      />

      <button type="submit">Submit Assessments</button>
    </form>
  );
};

export default ClimbingAssessmentForm;
