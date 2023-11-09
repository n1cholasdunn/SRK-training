import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {FitnessAssessmentFormValues} from '../../types/assessments/fitness';
import {useEffect, useMemo, useRef} from 'react';
import SharkSkillsSide from './SharkSkillsSide';

type Props = {
  control: Control<FitnessAssessmentFormValues>;
  register: UseFormRegister<FitnessAssessmentFormValues>;
  errors?: FieldErrors<FitnessAssessmentFormValues>;
};

const SharkSkillsAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'shark_skills.tests',
  });

  const initialRender = useRef(true);

  // useEffect(() => {
  //   console.log(fields);
  // }, [fields]);

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
          <SharkSkillsSide
            register={register}
            index={index}
            side="practice_left"
            errors={errors}
          />
          <SharkSkillsSide
            register={register}
            index={index}
            side="practice_right"
            errors={errors}
          />
          <SharkSkillsSide
            register={register}
            index={index}
            side="first_left"
            errors={errors}
          />
          <SharkSkillsSide
            register={register}
            index={index}
            side="first_right"
            errors={errors}
          />

          <SharkSkillsSide
            register={register}
            index={index}
            side="second_left"
            errors={errors}
          />
          <SharkSkillsSide
            register={register}
            index={index}
            side="second_right"
            errors={errors}
          />

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
