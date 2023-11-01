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

const OAFingerStrengthAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'oa_finger_strength.assessments',
  });

  useEffect(() => {
    if (fields.length === 0) {
      append({
        left: undefined,
        right: undefined,
        left_percentage: undefined,
        right_percentage: undefined,
      });
    }
  }, [fields, append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(
              `oa_finger_strength.assessments.${index}.left` as const
            )}
            defaultValue={undefined}
            placeholder="Total load Left Hand"
          />
          {errors?.oa_finger_strength?.assessments?.[index]?.left && (
            <p className={'text-red-500 px-2'}>
              {errors?.oa_finger_strength?.assessments?.[index]?.left?.message}
            </p>
          )}

          <input
            {...register(
              `oa_finger_strength.assessments.${index}.right` as const
            )}
            defaultValue={undefined}
            placeholder="Total load Right Hand"
          />
          {errors?.oa_finger_strength?.assessments?.[index]?.right && (
            <p className={'text-red-500 px-2'}>
              {errors?.oa_finger_strength?.assessments?.[index]?.right?.message}
            </p>
          )}
          <input
            {...register(
              `oa_finger_strength.assessments.${index}.left_percentage` as const
            )}
            defaultValue={undefined}
            placeholder="% of Bodyweight Left Hand"
          />
          {errors?.oa_finger_strength?.assessments?.[index]
            ?.left_percentage && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.oa_finger_strength?.assessments?.[index]
                  ?.left_percentage?.message
              }
            </p>
          )}

          <input
            {...register(
              `oa_finger_strength.assessments.${index}.right_percentage` as const
            )}
            defaultValue={undefined}
            placeholder="% of Bodyweight Right Hand"
          />
          {errors?.oa_finger_strength?.assessments?.[index]
            ?.right_percentage && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.oa_finger_strength?.assessments?.[index]
                  ?.right_percentage?.message
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
            left: undefined,
            right: undefined,
            left_percentage: undefined,
            right_percentage: undefined,
          })
        }>
        Add One Arm Finger Strength Test
      </button>
    </>
  );
};

export default OAFingerStrengthAssessment;
