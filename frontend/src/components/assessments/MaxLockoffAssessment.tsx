import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {AssessmentFormValues} from '../../types/assessments/climbing';
import {useEffect, useRef} from 'react';

type Props = {
  control: Control<AssessmentFormValues>;
  register: UseFormRegister<AssessmentFormValues>;
  errors?: FieldErrors<AssessmentFormValues>;
};

const MaxLockoffAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'max_lockoff.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({seconds: undefined});
      initialRender.current = false;
    }
  }, [fields, append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`max_lockoff.tests.${index}.seconds` as const)}
            defaultValue={undefined}
            placeholder="Seconds"
          />
          {errors?.max_lockoff?.tests?.[index]?.seconds && (
            <p className={'text-red-500 px-2'}>
              {errors?.max_lockoff?.tests?.[index]?.seconds?.message}
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
