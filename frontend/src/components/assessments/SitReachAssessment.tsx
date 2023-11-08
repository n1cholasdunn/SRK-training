import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {FitnessAssessmentFormValues} from '../../types/assessments/fitness';
import {useEffect, useRef} from 'react';

type Props = {
  control: Control<FitnessAssessmentFormValues>;
  register: UseFormRegister<FitnessAssessmentFormValues>;
  errors?: FieldErrors<FitnessAssessmentFormValues>;
};

const SitReachAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'sit_reach.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({
        first_measurement: undefined,
        second_measurement: undefined,
        third_measurement: undefined,
      });

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`sit_reach.tests.${index}.first_measurement` as const)}
            defaultValue={undefined}
            placeholder="First Measurement"
          />
          {errors?.sit_reach?.tests?.[index]?.first_measurement && (
            <p className={'text-red-500 px-2'}>
              {errors?.sit_reach?.tests?.[index]?.first_measurement?.message}
            </p>
          )}
          <input
            {...register(
              `sit_reach.tests.${index}.second_measurement` as const
            )}
            defaultValue={undefined}
            placeholder="Second Measurement"
          />
          {errors?.sit_reach?.tests?.[index]?.second_measurement && (
            <p className={'text-red-500 px-2'}>
              {errors?.sit_reach?.tests?.[index]?.second_measurement?.message}
            </p>
          )}
          <input
            {...register(`sit_reach.tests.${index}.third_measurement` as const)}
            defaultValue={undefined}
            placeholder="Third Measurement"
          />
          {errors?.sit_reach?.tests?.[index]?.third_measurement && (
            <p className={'text-red-500 px-2'}>
              {errors?.sit_reach?.tests?.[index]?.third_measurement?.message}
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
            first_measurement: undefined,
            second_measurement: undefined,
            third_measurement: undefined,
          })
        }>
        Add Sit and Reach Test
      </button>
    </>
  );
};

export default SitReachAssessment;
