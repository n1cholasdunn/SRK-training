import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {AssessmentFormValues} from '../../types/assessments/fitness';
import {useEffect, useRef} from 'react';

type Props = {
  control: Control<AssessmentFormValues>;
  register: UseFormRegister<AssessmentFormValues>;
  errors?: FieldErrors<AssessmentFormValues>;
};

const SitReachAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'sit_reach.assessments',
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
            {...register(
              `sit_reach.assessments.${index}.first_measurement` as const
            )}
            defaultValue={undefined}
            placeholder="First Measurement"
          />
          {errors?.sit_reach?.assessments?.[index]?.first_measurement && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.sit_reach?.assessments?.[index]?.first_measurement
                  ?.message
              }
            </p>
          )}
          <input
            {...register(
              `sit_reach.assessments.${index}.second_measurement` as const
            )}
            defaultValue={undefined}
            placeholder="Second Measurement"
          />
          {errors?.sit_reach?.assessments?.[index]?.second_measurement && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.sit_reach?.assessments?.[index]?.second_measurement
                  ?.message
              }
            </p>
          )}
          <input
            {...register(
              `sit_reach.assessments.${index}.third_measurement` as const
            )}
            defaultValue={undefined}
            placeholder="Third Measurement"
          />
          {errors?.sit_reach?.assessments?.[index]?.third_measurement && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.sit_reach?.assessments?.[index]?.third_measurement
                  ?.message
              }
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
