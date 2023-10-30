import {zodResolver} from '@hookform/resolvers/zod';
import {Controller, useForm} from 'react-hook-form';
import {
  ProgramFormValues,
  ProgramInfoSchema,
  programOptions,
  trainingStyles,
} from '../../types/programInfo';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import {useState} from 'react';
import ClimbTypeCheckbox from '../climbTypeCheckbox';
import {
  fontBoulderingGrades,
  sportFrenchGrades,
  sportYDSGrades,
  vBoulderingGrades,
} from '../../utils/climbingGrades';

const ClientProgramForm = () => {
  const [gradingSystem, setGradingSystem] = useState('');
  const [climbingType, setClimbingType] = useState('');

  const {
    handleSubmit,
    formState: {errors},
    register,
    control,
  } = useForm<ProgramFormValues>({
    resolver: zodResolver(ProgramInfoSchema),
    defaultValues: {program_start: new Date()},
  });

  const handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const system = e.target.id;
    const isChecked = e.target.checked;
    if (!isChecked) {
      setGradingSystem('');
      return;
    }

    setGradingSystem(system);
  };

  const handleClimbCheckboxChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const system = e.target.id;
    const isChecked = e.target.checked;
    if (!isChecked) {
      setClimbingType('');
      return;
    }

    setClimbingType(system);
  };

  // useEffect(() => {
  //   console.log(gradingSystem);
  // }, [gradingSystem]);

  const onSubmit = (data: ProgramFormValues) => {
    try {
      ProgramInfoSchema.parse(data);
      console.log(data);

      // TODO add submit logic
    } catch (error) {
      // TODO add error handling
    }
  };

  const renderGradeOptions = () => {
    if (gradingSystem === 'na-grading' && climbingType === 'bouldering') {
      return vBoulderingGrades.map(grade => (
        <option value={grade} key={grade}>
          {grade}
        </option>
      ));
    }
    if (gradingSystem === 'na-grading' && climbingType === 'sport') {
      return sportYDSGrades.map(grade => (
        <option value={grade} key={grade}>
          {grade}
        </option>
      ));
    }
    if (gradingSystem === 'eu-grading' && climbingType === 'bouldering') {
      return fontBoulderingGrades.map(grade => (
        <option value={grade} key={grade}>
          {grade}
        </option>
      ));
    }
    if (gradingSystem === 'eu-grading' && climbingType === 'sport') {
      return sportFrenchGrades.map(grade => (
        <option value={grade} key={grade}>
          {grade}
        </option>
      ));
    }
  };

  return (
    <div>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex flex-col space-y-3">
        <div>
          Program Type:
          <select {...register('program_type')}>
            {programOptions &&
              programOptions.map((program, index) => (
                <option value={program} key={index} placeholder="Program Type">
                  {program}
                </option>
              ))}
          </select>
          {errors.program_type && (
            <p className={'text-red-500 px-2'}>
              {errors.program_type?.message}
            </p>
          )}
        </div>
        <div>
          Training Style:
          <select {...register('training_style')}>
            {trainingStyles &&
              trainingStyles.map((style, index) => (
                <option value={style} key={index}>
                  {style}
                </option>
              ))}
          </select>
          {errors.training_style && (
            <p className={'text-red-500 px-2'}>
              {errors.training_style?.message}
            </p>
          )}
        </div>
        <div>
          Choose Date:
          <Controller
            name={'program_start'}
            control={control}
            render={({field: {onChange, value}}) => (
              <DatePicker
                selected={value}
                onChange={onChange}
                placeholderText="Choose Date"
                className="px-2"
              />
            )}
          />
          {errors.program_start && (
            <p className={'text-red-500 px-2'}>
              {errors.program_start?.message}
            </p>
          )}
        </div>
        <div className="flex justify-evenly">
          <label htmlFor="na-grading">V-Grades/YDS Grades(US Grading)</label>
          <input
            type="checkbox"
            id="na-grading"
            checked={gradingSystem === 'na-grading'}
            onChange={handleCheckboxChange}
          />

          <label htmlFor="eu-grading">Font/French Grades(EU Grading)</label>
          <input
            type="checkbox"
            id="eu-grading"
            checked={gradingSystem === 'eu-grading'}
            onChange={handleCheckboxChange}
          />
          <ClimbTypeCheckbox
            climbingType={climbingType}
            handleClimbCheckboxChange={handleClimbCheckboxChange}
          />
        </div>
        <div className="flex space-x-2">
          <label htmlFor="outdoor-max">Outdoor Max:</label>
          {/* TODO conditionally render based off first select of boulders or sport and font/french grading or vscale/yds */}
          <select {...register('outdoor_max')} id="outdoor-max">
            {renderGradeOptions()}
          </select>
          {errors.outdoor_max && (
            <p className={'text-red-500 px-2'}>{errors.outdoor_max?.message}</p>
          )}
        </div>
        <div className="flex space-x-2">
          <label htmlFor="outdoor-flash">Outdoor Flash:</label>
          <select {...register('outdoor_flash')} id="outdoor-flash">
            {renderGradeOptions()}
          </select>
          {errors.outdoor_flash && (
            <p className={'text-red-500 px-2'}>
              {errors.outdoor_flash?.message}
            </p>
          )}
        </div>
        <div className="flex space-x-2">
          <label htmlFor="indoor-max">Indoor Max:</label>
          <select {...register('indoor_max')} id="indoor-max">
            {renderGradeOptions()}
          </select>
          {errors.indoor_max && (
            <p className={'text-red-500 px-2'}>{errors.indoor_max?.message}</p>
          )}
        </div>
        <div className="flex space-x-2">
          <label htmlFor="indoor-flash">Indoor Flash:</label>
          <select {...register('indoor_flash')} id="indoor-flash">
            {renderGradeOptions()}
          </select>
          {errors.indoor_flash && (
            <p className={'text-red-500 px-2'}>
              {errors.indoor_flash?.message}
            </p>
          )}
        </div>

        <button
          type="submit"
          className="bg-red-200 rounded-md w-1/3 self-center">
          Submit Program Info
        </button>
        {/* <GradeSelection register={register} /> */}
      </form>
    </div>
  );
};

export default ClientProgramForm;
