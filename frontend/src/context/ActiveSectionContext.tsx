import React, {useState, createContext} from 'react';
import type {SectionName} from '../types/sections';

type ActiveSectionContextType = {
  activeSection: SectionName;
  setActiveSection: React.Dispatch<React.SetStateAction<SectionName>>;
  timeOfPrevClick: number;
  setTimeOfPrevClick: React.Dispatch<React.SetStateAction<number>>;
};

export const ActiveSectionContext =
  createContext<ActiveSectionContextType | null>(null);

type Props = {
  children: React.ReactNode;
};
const ActiveSectionContextProvider = ({children}: Props) => {
  const [activeSection, setActiveSection] = useState<SectionName>('Home');
  const [timeOfPrevClick, setTimeOfPrevClick] = useState(0);
  return (
    <ActiveSectionContext.Provider
      value={{
        activeSection,
        setActiveSection,
        timeOfPrevClick,
        setTimeOfPrevClick,
      }}>
      {children}
    </ActiveSectionContext.Provider>
  );
};
export default ActiveSectionContextProvider;
