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

const YMCAStepAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'ymca_step.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({recovery_hr: undefined, rating: ''});

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`ymca_step.tests.${index}.recovery_hr` as const)}
            defaultValue={undefined}
            placeholder="Recovery HR"
          />
          {errors?.ymca_step?.tests?.[index]?.recovery_hr && (
            <p className={'text-red-500 px-2'}>
              {errors?.ymca_step?.tests?.[index]?.recovery_hr?.message}
            </p>
          )}
          <input
            {...register(`ymca_step.tests.${index}.rating` as const)}
            defaultValue={undefined}
            placeholder="Rating"
          />
          {errors?.ymca_step?.tests?.[index]?.rating && (
            <p className={'text-red-500 px-2'}>
              {errors?.ymca_step?.tests?.[index]?.rating?.message}
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
        onClick={() => append({recovery_hr: undefined, rating: ''})}>
        Add YMCA Step Test
      </button>
    </>
  );
};

export default YMCAStepAssessment;
