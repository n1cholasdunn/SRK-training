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

const HealthMarkersAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'health_markers.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({
        weight: undefined,
        bmi: undefined,
        waist_hip_ratio: undefined,
        resting_hr: undefined,
        blood_pressure: undefined,
        vo2_max: undefined,
      });

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`health_markers.tests.${index}.weight` as const)}
            defaultValue={undefined}
            placeholder="Weight"
          />
          {errors?.health_markers?.tests?.[index]?.weight && (
            <p className={'text-red-500 px-2'}>
              {errors?.health_markers?.tests?.[index]?.weight?.message}
            </p>
          )}
          <input
            {...register(`health_markers.tests.${index}.bmi` as const)}
            defaultValue={undefined}
            placeholder="BMI"
          />
          {errors?.health_markers?.tests?.[index]?.bmi && (
            <p className={'text-red-500 px-2'}>
              {errors?.health_markers?.tests?.[index]?.bmi?.message}
            </p>
          )}
          <input
            {...register(
              `health_markers.tests.${index}.waist_hip_ratio` as const
            )}
            defaultValue={undefined}
            placeholder="Waist-Hip Ratio"
          />
          {errors?.health_markers?.tests?.[index]?.waist_hip_ratio && (
            <p className={'text-red-500 px-2'}>
              {errors?.health_markers?.tests?.[index]?.waist_hip_ratio?.message}
            </p>
          )}
          <input
            {...register(`health_markers.tests.${index}.resting_hr` as const)}
            defaultValue={undefined}
            placeholder="Resting HR"
          />
          {errors?.health_markers?.tests?.[index]?.resting_hr && (
            <p className={'text-red-500 px-2'}>
              {errors?.health_markers?.tests?.[index]?.resting_hr?.message}
            </p>
          )}
          <input
            {...register(
              `health_markers.tests.${index}.blood_pressure` as const
            )}
            defaultValue={undefined}
            placeholder="Blood Pressure"
          />
          {errors?.health_markers?.tests?.[index]?.blood_pressure && (
            <p className={'text-red-500 px-2'}>
              {errors?.health_markers?.tests?.[index]?.blood_pressure?.message}
            </p>
          )}
          <input
            {...register(`health_markers.tests.${index}.vo2_max` as const)}
            defaultValue={undefined}
            placeholder="VO2 Max"
          />
          {errors?.health_markers?.tests?.[index]?.vo2_max && (
            <p className={'text-red-500 px-2'}>
              {errors?.health_markers?.tests?.[index]?.vo2_max?.message}
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
            weight: undefined,
            bmi: undefined,
            waist_hip_ratio: undefined,
            resting_hr: undefined,
            blood_pressure: undefined,
            vo2_max: undefined,
          })
        }>
        Add Health Markers Test
      </button>
    </>
  );
};

export default HealthMarkersAssessment;
