import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {ClimbingAssessmentFormValues} from '../../types/assessments/climbing';
import {useEffect, useRef} from 'react';

type Props = {
  control: Control<ClimbingAssessmentFormValues>;
  register: UseFormRegister<ClimbingAssessmentFormValues>;
  errors?: FieldErrors<ClimbingAssessmentFormValues>;
};

const OAPinchAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'oa_pinch_strength.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({left: undefined, right: undefined});
      initialRender.current = false;
    }
  }, [append]);
  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`oa_pinch_strength.tests.${index}.left` as const)}
            defaultValue={undefined}
            placeholder="Left"
          />
          {errors?.oa_pinch_strength?.tests?.[index]?.left && (
            <p className={'text-red-500 px-2'}>
              {errors?.oa_pinch_strength?.tests?.[index]?.left?.message}
            </p>
          )}

          <input
            {...register(`oa_pinch_strength.tests.${index}.right` as const)}
            defaultValue={undefined}
            placeholder="Right"
          />
          {errors?.oa_pinch_strength?.tests?.[index]?.right && (
            <p className={'text-red-500 px-2'}>
              {errors?.oa_pinch_strength?.tests?.[index]?.right?.message}
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
