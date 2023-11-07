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

const MeasurementsAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'measurements.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({
        chest: undefined,
        biceps: undefined,
        forearms: undefined,
        lower_abdomen: undefined,
        hips: undefined,
        upper_thigh: undefined,
        mid_thigh: undefined,
        calves: undefined,
      });

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`measurements.tests.${index}.chest` as const)}
            defaultValue={undefined}
            placeholder="Chest"
          />
          {errors?.measurements?.tests?.[index]?.chest && (
            <p className={'text-red-500 px-2'}>
              {errors?.measurements?.tests?.[index]?.chest?.message}
            </p>
          )}
          <input
            {...register(`measurements.tests.${index}.biceps` as const)}
            defaultValue={undefined}
            placeholder="Biceps"
          />
          {errors?.measurements?.tests?.[index]?.biceps && (
            <p className={'text-red-500 px-2'}>
              {errors?.measurements?.tests?.[index]?.biceps?.message}
            </p>
          )}
          <input
            {...register(`measurements.tests.${index}.forearms` as const)}
            defaultValue={undefined}
            placeholder="Forearms"
          />
          {errors?.measurements?.tests?.[index]?.forearms && (
            <p className={'text-red-500 px-2'}>
              {errors?.measurements?.tests?.[index]?.forearms?.message}
            </p>
          )}
          <input
            {...register(`measurements.tests.${index}.lower_abdomen` as const)}
            defaultValue={undefined}
            placeholder="Lower Abdomen"
          />
          {errors?.measurements?.tests?.[index]?.lower_abdomen && (
            <p className={'text-red-500 px-2'}>
              {errors?.measurements?.tests?.[index]?.lower_abdomen?.message}
            </p>
          )}
          <input
            {...register(`measurements.tests.${index}.hips` as const)}
            defaultValue={undefined}
            placeholder="Hips"
          />
          {errors?.measurements?.tests?.[index]?.hips && (
            <p className={'text-red-500 px-2'}>
              {errors?.measurements?.tests?.[index]?.hips?.message}
            </p>
          )}
          <input
            {...register(`measurements.tests.${index}.upper_thigh` as const)}
            defaultValue={undefined}
            placeholder="Upper Thigh"
          />
          {errors?.measurements?.tests?.[index]?.upper_thigh && (
            <p className={'text-red-500 px-2'}>
              {errors?.measurements?.tests?.[index]?.upper_thigh?.message}
            </p>
          )}
          <input
            {...register(`measurements.tests.${index}.mid_thigh` as const)}
            defaultValue={undefined}
            placeholder="Mid Thigh"
          />
          {errors?.measurements?.tests?.[index]?.mid_thigh && (
            <p className={'text-red-500 px-2'}>
              {errors?.measurements?.tests?.[index]?.mid_thigh?.message}
            </p>
          )}
          <input
            {...register(`measurements.tests.${index}.calves` as const)}
            defaultValue={undefined}
            placeholder="Calves"
          />
          {errors?.measurements?.tests?.[index]?.calves && (
            <p className={'text-red-500 px-2'}>
              {errors?.measurements?.tests?.[index]?.calves?.message}
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
            chest: undefined,
            biceps: undefined,
            forearms: undefined,
            lower_abdomen: undefined,
            hips: undefined,
            upper_thigh: undefined,
            mid_thigh: undefined,
            calves: undefined,
          })
        }>
        Add Measurements Test
      </button>
    </>
  );
};

export default MeasurementsAssessment;
