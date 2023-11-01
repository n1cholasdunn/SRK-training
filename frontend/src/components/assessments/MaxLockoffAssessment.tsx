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

const MaxLockoffAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'max_lockoff.assessments',
  });

  useEffect(() => {
    if (fields.length === 0) {
      append({seconds: undefined});
    }
  }, [fields, append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`max_lockoff.assessments.${index}.seconds` as const)}
            defaultValue={undefined}
            placeholder="Seconds"
          />
          {errors?.max_lockoff?.assessments?.[index]?.seconds && (
            <p className={'text-red-500 px-2'}>
              {errors?.max_lockoff?.assessments?.[index]?.seconds?.message}
            </p>
          )}
          {fields.length > 1 && (
            <button type="button" onClick={() => remove(index)}>
              Remove
            </button>
          )}
        </div>
      ))}
      <button type="button" onClick={() => append({seconds: undefined})}>
        Add Max Lockoff Test
      </button>
    </>
  );
};

export default MaxLockoffAssessment;
