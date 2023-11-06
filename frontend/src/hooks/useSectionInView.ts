import {useInView} from 'react-intersection-observer';
import {useActiveSectionContext} from './useActiveSectionContext';
import {useEffect} from 'react';
import type {SectionName} from '../types/sections';

export const useSectionInView = (
  sectionName: SectionName,
  threshold = 0.75
) => {
  const {ref, inView} = useInView({
    threshold: threshold,
  });
  const {setActiveSection, timeOfPrevClick} = useActiveSectionContext();

  useEffect(() => {
    if (inView && Date.now() - timeOfPrevClick > 1000)
      setActiveSection(sectionName);
  }, [inView, setActiveSection, timeOfPrevClick, sectionName]);

  return {ref};
};
