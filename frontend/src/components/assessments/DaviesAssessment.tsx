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

const DaviesAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'davies.assessments',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({
        first_trial: undefined,
        second_trial: undefined,
        third_trial: undefined,
      });

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`davies.assessments.${index}.first_trial` as const)}
            defaultValue={undefined}
            placeholder="First Trial"
          />
          {errors?.davies?.assessments?.[index]?.first_trial && (
            <p className={'text-red-500 px-2'}>
              {errors?.davies?.assessments?.[index]?.first_trial?.message}
            </p>
          )}
          <input
            {...register(`davies.assessments.${index}.second_trial` as const)}
            defaultValue={undefined}
            placeholder="Second Trial"
          />
          {errors?.davies?.assessments?.[index]?.second_trial && (
            <p className={'text-red-500 px-2'}>
              {errors?.davies?.assessments?.[index]?.second_trial?.message}
            </p>
          )}
          <input
            {...register(`davies.assessments.${index}.third_trial` as const)}
            defaultValue={undefined}
            placeholder="Third Trial"
          />
          {errors?.davies?.assessments?.[index]?.third_trial && (
            <p className={'text-red-500 px-2'}>
              {errors?.davies?.assessments?.[index]?.third_trial?.message}
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
            first_trial: undefined,
            second_trial: undefined,
            third_trial: undefined,
          })
        }>
        Add Davies Test
      </button>
    </>
  );
};

export default DaviesAssessment;
