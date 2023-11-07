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

const PowerEnduranceAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'power_endurance.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({seconds: undefined});

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`power_endurance.tests.${index}.seconds` as const)}
            defaultValue={undefined}
            placeholder="Seconds"
          />
          {errors?.power_endurance?.tests?.[index]?.seconds && (
            <p className={'text-red-500 px-2'}>
              {errors?.power_endurance?.tests?.[index]?.seconds?.message}
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
        Add Power Endurance Test
      </button>
    </>
  );
};

export default PowerEnduranceAssessment;
