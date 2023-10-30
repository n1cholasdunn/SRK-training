import {ChangeEvent} from 'react';

type Props = {
  climbingType: string;
  handleClimbCheckboxChange: (e: ChangeEvent<HTMLInputElement>) => void;
};

const ClimbTypeCheckbox = ({
  climbingType,
  handleClimbCheckboxChange,
}: Props) => {
  return (
    <>
      <label htmlFor="bouldering">Bouldering</label>
      <input
        type="checkbox"
        id="bouldering"
        checked={climbingType === 'bouldering'}
        onChange={handleClimbCheckboxChange}
      />
      <label htmlFor="sport">Sport</label>
      <input
        type="checkbox"
        id="sport"
        checked={climbingType === 'sport'}
        onChange={handleClimbCheckboxChange}
      />
    </>
  );
};

export default ClimbTypeCheckbox;
