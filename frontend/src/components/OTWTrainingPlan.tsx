import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {useEffect, useRef} from 'react';
import {TrainingFormValues} from '../types/training';

type Props = {
  control: Control<TrainingFormValues>;
  register: UseFormRegister<TrainingFormValues>;
  errors?: FieldErrors<TrainingFormValues>;
};

const OTWTrainingPlan = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'otw_training.exercises',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({
        name: '',
        equipment_used: '',
        rest: '',
        sets: '',
        notes: '',
      });

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <textarea
            {...register(`otw_training.warmup` as const)}
            defaultValue={undefined}
            placeholder="Warmup"
          />
          {errors?.otw_training?.warmup && (
            <p className={'text-red-500 px-2'}>
              {errors?.otw_training?.warmup?.message}
            </p>
          )}
          <input
            {...register(`otw_training.exercises.${index}.name` as const)}
            defaultValue={undefined}
            placeholder="Name"
          />
          {errors?.otw_training?.exercises?.[index]?.name && (
            <p className={'text-red-500 px-2'}>
              {errors?.otw_training?.exercises?.[index]?.name?.message}
            </p>
          )}
          <input
            {...register(
              `otw_training.exercises.${index}.equipment_used` as const
            )}
            defaultValue={undefined}
            placeholder="Equipment Used"
          />
          {errors?.otw_training?.exercises?.[index]?.equipment_used && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.otw_training?.exercises?.[index]?.equipment_used
                  ?.message
              }
            </p>
          )}
          <input
            {...register(`otw_training.exercises.${index}.rest` as const)}
            defaultValue={undefined}
            placeholder="Rest"
          />
          {errors?.otw_training?.exercises?.[index]?.rest && (
            <p className={'text-red-500 px-2'}>
              {errors?.otw_training?.exercises?.[index]?.rest?.message}
            </p>
          )}
          <input
            {...register(`otw_training.exercises.${index}.sets` as const)}
            defaultValue={undefined}
            placeholder="Sets"
          />
          {errors?.otw_training?.exercises?.[index]?.sets && (
            <p className={'text-red-500 px-2'}>
              {errors?.otw_training?.exercises?.[index]?.sets?.message}
            </p>
          )}
          <textarea
            {...register(`otw_training.exercises.${index}.notes` as const)}
            defaultValue={undefined}
            placeholder="Notes"
          />
          {errors?.otw_training?.exercises?.[index]?.notes && (
            <p className={'text-red-500 px-2'}>
              {errors?.otw_training?.exercises?.[index]?.notes?.message}
            </p>
          )}

          {fields.length > 1 && (
            <button type="button" onClick={() => remove(index)}>
              Remove
            </button>
          )}
        </div>
      ))}
      <button
        type="button"
        onClick={() =>
          append({
            name: '',
            equipment_used: '',
            rest: '',
            sets: '',
            notes: '',
          })
        }>
        Add OTW Training Exercise
      </button>
    </>
  );
};

export default OTWTrainingPlan;
