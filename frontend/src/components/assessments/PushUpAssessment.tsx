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

const PushUpAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'pushup.assessments',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({num_pushups: undefined, completed: false});

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`pushup.assessments.${index}.num_pushups` as const)}
            defaultValue={undefined}
            placeholder="# of Pushups"
          />
          {errors?.pushup?.assessments?.[index]?.num_pushups && (
            <p className={'text-red-500 px-2'}>
              {errors?.pushup?.assessments?.[index]?.num_pushups?.message}
            </p>
          )}
          <label htmlFor="pushup-checkbox">Completed(Y/N): </label>
          <input
            type="checkbox"
            id="pushup-checkbox"
            {...register(`pushup.assessments.${index}.completed` as const)}
            defaultValue={'false'}
          />
          {errors?.pushup?.assessments?.[index]?.completed && (
            <p className={'text-red-500 px-2'}>
              {errors?.pushup?.assessments?.[index]?.completed?.message}
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
        onClick={() => append({num_pushups: undefined, completed: false})}>
        Add Pushup Test
      </button>
    </>
  );
};

export default PushUpAssessment;
