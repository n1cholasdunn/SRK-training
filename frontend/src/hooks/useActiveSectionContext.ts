import {useContext} from 'react';
import {ActiveSectionContext} from '../context/ActiveSectionContext';

export const useActiveSectionContext = () => {
  const context = useContext(ActiveSectionContext);

  if (context === null) {
    throw new Error(
      'useActiveSection context must be used from within the ActiveSectionContextProvider'
    );
  }
  return context;
};
