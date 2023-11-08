import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {type FitnessAssessmentFormValues} from '../../types/assessments/fitness';
import {useEffect, useRef} from 'react';

type Props = {
  control: Control<FitnessAssessmentFormValues>;
  register: UseFormRegister<FitnessAssessmentFormValues>;
  errors?: FieldErrors<FitnessAssessmentFormValues>;
};

const CoreAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'core.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({first_trial: undefined, second_trial: undefined});

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`core.tests.${index}.first_trial` as const)}
            defaultValue={undefined}
            placeholder="First Trial"
          />
          {errors?.core?.tests?.[index]?.first_trial && (
            <p className={'text-red-500 px-2'}>
              {errors?.core?.tests?.[index]?.first_trial?.message}
            </p>
          )}
          <input
            {...register(`core.tests.${index}.second_trial` as const)}
            defaultValue={undefined}
            placeholder="Second Trial"
          />
          {errors?.core?.tests?.[index]?.second_trial && (
            <p className={'text-red-500 px-2'}>
              {errors?.core?.tests?.[index]?.second_trial?.message}
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
          append({first_trial: undefined, second_trial: undefined})
        }>
        Add Core Test
      </button>
    </>
  );
};

export default CoreAssessment;
