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
const MaxPullupsAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'max_pullups.assessments',
  });

  useEffect(() => {
    if (fields.length === 0) {
      append({reps: undefined});
    }
  }, [fields, append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`max_pullups.assessments.${index}.reps` as const)}
            defaultValue={undefined}
            placeholder="Reps"
          />
          {errors?.max_pullups?.assessments?.[index]?.reps && (
            <p className={'text-red-500 px-2'}>
              {errors?.max_pullups?.assessments?.[index]?.reps?.message}
            </p>
          )}
          {fields.length > 1 && (
            <button type="button" onClick={() => remove(index)}>
              Remove
            </button>
          )}
        </div>
      ))}
      <button type="button" onClick={() => append({reps: undefined})}>
        Add Max Pullups Test
      </button>
    </>
  );
};

export default MaxPullupsAssessment;
