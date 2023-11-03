import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {AssessmentFormValues} from '../../types/assessments/fitness';
import {useEffect, useMemo, useRef} from 'react';

type Props = {
  control: Control<AssessmentFormValues>;
  register: UseFormRegister<AssessmentFormValues>;
  errors?: FieldErrors<AssessmentFormValues>;
};

const SharkSkillsAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'shark_skills.assessments',
  });
  // const emptySide = {
  //   time: undefined,
  //   deduction_tally: undefined,
  //   total_deducted: undefined,
  //   final_total: undefined,
  // };

  const initialRender = useRef(true);

  const emptySide = useMemo(
    () => ({
      time: undefined,
      deduction_tally: undefined,
      total_deducted: undefined,
      final_total: undefined,
    }),
    []
  );

  const emptyTest = useMemo(
    () => ({
      practice_left: emptySide,
      practice_right: emptySide,
      first_left: emptySide,
      first_right: emptySide,
      second_left: emptySide,
      second_right: emptySide,
    }),
    [emptySide]
  );
  // const emptyTest = {
  //   practice_left: emptySide,
  //   practice_right: emptySide,
  //   first_left: emptySide,
  //   first_right: emptySide,
  //   second_left: emptySide,
  //   second_right: emptySide,
  // };
  useEffect(() => {
    if (initialRender.current) {
      append(emptyTest);

      initialRender.current = false;
    }
  }, [append, emptyTest]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(
              `shark_skills.assessments.${index}.practice_left` as const
            )}
            defaultValue={undefined}
            placeholder="Practice Left"
          />
          {errors?.shark_skills?.assessments?.[index]?.practice_left && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.shark_skills?.assessments?.[index]?.practice_left
                  ?.message
              }
            </p>
          )}
          <input
            {...register(
              `shark_skills.assessments.${index}.practice_right` as const
            )}
            defaultValue={undefined}
            placeholder="Practice Right"
          />
          {errors?.shark_skills?.assessments?.[index]?.practice_right && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.shark_skills?.assessments?.[index]?.practice_right
                  ?.message
              }
            </p>
          )}
          <input
            {...register(
              `shark_skills.assessments.${index}.first_left` as const
            )}
            defaultValue={undefined}
            placeholder="First Left"
          />
          {errors?.shark_skills?.assessments?.[index]?.first_left && (
            <p className={'text-red-500 px-2'}>
              {errors?.shark_skills?.assessments?.[index]?.first_left?.message}
            </p>
          )}
          <input
            {...register(
              `shark_skills.assessments.${index}.first_right` as const
            )}
            defaultValue={undefined}
            placeholder="First Right"
          />
          {errors?.shark_skills?.assessments?.[index]?.first_right && (
            <p className={'text-red-500 px-2'}>
              {errors?.shark_skills?.assessments?.[index]?.first_right?.message}
            </p>
          )}
          <input
            {...register(
              `shark_skills.assessments.${index}.second_left` as const
            )}
            defaultValue={undefined}
            placeholder="Second Left"
          />
          {errors?.shark_skills?.assessments?.[index]?.second_left && (
            <p className={'text-red-500 px-2'}>
              {errors?.shark_skills?.assessments?.[index]?.second_left?.message}
            </p>
          )}
          <input
            {...register(
              `shark_skills.assessments.${index}.second_right` as const
            )}
            defaultValue={undefined}
            placeholder="Second Right"
          />
          {errors?.shark_skills?.assessments?.[index]?.second_right && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.shark_skills?.assessments?.[index]?.second_right
                  ?.message
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
      <button type="button" onClick={() => append(emptyTest)}>
        Add Shark Skills Test
      </button>
    </>
  );
};

export default SharkSkillsAssessment;
