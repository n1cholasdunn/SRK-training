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

const OverheadSquatAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'overhead_squat.assessments',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({foot_ankle: '', knee: '', lphc: '', shoulder: '', solutions: ''});

      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(
              `overhead_squat.assessments.${index}.foot_ankle` as const
            )}
            defaultValue={undefined}
            placeholder="Foot & Ankle"
          />
          {errors?.overhead_squat?.assessments?.[index]?.foot_ankle && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.overhead_squat?.assessments?.[index]?.foot_ankle
                  ?.message
              }
            </p>
          )}
          <input
            {...register(`overhead_squat.assessments.${index}.knee` as const)}
            defaultValue={undefined}
            placeholder="Knee"
          />
          {errors?.overhead_squat?.assessments?.[index]?.knee && (
            <p className={'text-red-500 px-2'}>
              {errors?.overhead_squat?.assessments?.[index]?.knee?.message}
            </p>
          )}
          <input
            {...register(`overhead_squat.assessments.${index}.lphc` as const)}
            defaultValue={undefined}
            placeholder="LPHC"
          />
          {errors?.overhead_squat?.assessments?.[index]?.lphc && (
            <p className={'text-red-500 px-2'}>
              {errors?.overhead_squat?.assessments?.[index]?.lphc?.message}
            </p>
          )}
          <input
            {...register(
              `overhead_squat.assessments.${index}.shoulder` as const
            )}
            defaultValue={undefined}
            placeholder="Shoulder"
          />
          {errors?.overhead_squat?.assessments?.[index]?.shoulder && (
            <p className={'text-red-500 px-2'}>
              {errors?.overhead_squat?.assessments?.[index]?.shoulder?.message}
            </p>
          )}
          <textarea
            {...register(
              `overhead_squat.assessments.${index}.solutions` as const
            )}
            defaultValue={undefined}
            placeholder="Solutions"
          />
          {errors?.overhead_squat?.assessments?.[index]?.solutions && (
            <p className={'text-red-500 px-2'}>
              {errors?.overhead_squat?.assessments?.[index]?.solutions?.message}
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
            foot_ankle: '',
            knee: '',
            lphc: '',
            shoulder: '',
            solutions: '',
          })
        }>
        Add Overhead Squat Test
      </button>
    </>
  );
};

export default OverheadSquatAssessment;
