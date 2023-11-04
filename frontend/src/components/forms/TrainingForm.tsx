import {TrainingFormSchema, TrainingFormValues} from '../../types/training';
import {zodResolver} from '@hookform/resolvers/zod';
import {useForm} from 'react-hook-form';
import OTWTrainingPlan from '../OTWTrainingPlan';
import PrehabTrainingPlan from './PrehabTrainingPlan';
import GymTrainingPlan from './GymTrainingPlan';

const TrainingForm = () => {
  const {
    handleSubmit,
    register,
    control,
    formState: {errors},
  } = useForm<TrainingFormValues>({
    resolver: zodResolver(TrainingFormSchema),
  });

  const onSubmit = (data: TrainingFormValues) => {
    console.log(data);
  };
  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className=" flex flex-col space-y-2">
      <h2>OTW Training Plan</h2>
      <OTWTrainingPlan control={control} register={register} errors={errors} />
      <h2>Gym Training Plan</h2>
      <GymTrainingPlan control={control} register={register} errors={errors} />
      <h2>Prehab Training Plan</h2>
      <PrehabTrainingPlan
        control={control}
        register={register}
        errors={errors}
      />

      <button type="submit">Submit Training Plans</button>
    </form>
  );
};

export default TrainingForm;
