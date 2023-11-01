import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {AssessmentFormValues} from '../../types/assessments/climbing';
import {useEffect} from 'react';

type Props = {
  control: Control<AssessmentFormValues>;
  register: UseFormRegister<AssessmentFormValues>;
  errors?: FieldErrors<AssessmentFormValues>;
};

const OAPinchAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'oa_pinch_strength.assessments',
  });

  useEffect(() => {
    if (fields.length === 0) {
      append({left: undefined, right: undefined});
    }
  }, [fields, append]);
  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(
              `oa_pinch_strength.assessments.${index}.left` as const
            )}
            defaultValue={undefined}
            placeholder="Left"
          />
          {errors?.oa_pinch_strength?.assessments?.[index]?.left && (
            <p className={'text-red-500 px-2'}>
              {errors?.oa_pinch_strength?.assessments?.[index]?.left?.message}
            </p>
          )}

          <input
            {...register(
              `oa_pinch_strength.assessments.${index}.right` as const
            )}
            defaultValue={undefined}
            placeholder="Right"
          />
          {errors?.oa_pinch_strength?.assessments?.[index]?.right && (
            <p className={'text-red-500 px-2'}>
              {errors?.oa_pinch_strength?.assessments?.[index]?.right?.message}
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
        onClick={() => append({left: undefined, right: undefined})}>
        Add One Arm Pinch Test
      </button>
    </>
  );
};

export default OAPinchAssessment;
