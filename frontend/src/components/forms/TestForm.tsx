/* eslint-disable @typescript-eslint/no-unused-vars */
import {TOKEN_KEY} from '../../api';
import {zodResolver} from '@hookform/resolvers/zod';
import {
  ClimbingAssessmentFormSchema,
  ClimbingAssessmentFormValues,
} from '../../types/assessments/climbing';
import {useForm} from 'react-hook-form';
import PowerEnduranceAssessment from '../assessments/PowerEnduranceAssessment';
import MaxPullupsAssessment from '../assessments/MaxPullupsAssessment';
import MaxLockoffAssessment from '../assessments/MaxLockoffAssessment';
import FingerStrengthAssessment from '../assessments/FingerStrengthAssessment';
import OAFingerStrengthAssessment from '../assessments/OAFingerStrengthAssessment';
import OAPinchAssessment from '../assessments/OAPinchAssessment';

const TestAssessmentForm = () => {
  const {
    handleSubmit,
    register,
    control,
    formState: {errors},
  } = useForm<ClimbingAssessmentFormValues>({
    resolver: zodResolver(ClimbingAssessmentFormSchema),
  });
  const token = localStorage.getItem(TOKEN_KEY);

  const onSubmit = (data: ClimbingAssessmentFormValues) => {
    ClimbingAssessmentFormSchema.parse(data);
    console.log('data shape!!', data);

    fetch('http://127.0.0.1:8000/assessments/climbing/testing/create/', {
      method: 'POST',
      headers: {
        Authorization: `Token ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then(response => {
        if (response.ok) {
          console.log(response.json(), 'RESPONSE');
        } else {
          throw new Error('Server returned non-OK status: ' + response.status);
        }
      })
      .then(data => {
        console.log(data); // "Data inputted successfully!"
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
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
      {/* <h2>Max Pullups Assessment</h2>
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
      /> */}

      <button type="submit">Submit Assessments</button>
    </form>
  );
};

export default TestAssessmentForm;
