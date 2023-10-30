import {UseFormRegister} from 'react-hook-form';
import {ProgramFormValues} from '../types/programInfo';

type Props = {
  register: UseFormRegister<ProgramFormValues>;
};
const GradeSelection = ({register}: Props) => {
  return (
    <>
      <div className="flex space-x-2">
        <label htmlFor="outdoor-max">Outdoor Max:</label>
        {/* TODO conditionally render based off first select of boulders or sport and font/french grading or vscale/yds */}
        <select {...register('outdoor_max')} id="outdoor-max"></select>
      </div>
      <div className="flex space-x-2">
        <label htmlFor="outdoor-flash">Outdoor Flash:</label>
        <select {...register('outdoor_flash')} id="outdoor-flash"></select>
      </div>
      <div className="flex space-x-2">
        <label htmlFor="indoor-max">Indoor Max:</label>
        <select {...register('indoor_max')} id="indoor-max"></select>
      </div>
      <div className="flex space-x-2">
        <label htmlFor="indoor-flash">Indoor Flash:</label>
        <select {...register('indoor_flash')} id="indoor-flash"></select>
      </div>
    </>
  );
};

export default GradeSelection;
