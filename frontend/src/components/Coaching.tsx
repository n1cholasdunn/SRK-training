import {motion} from 'framer-motion';
import SectionHeading from './ui/SectionHeading';
import {useSectionInView} from '../hooks/useSectionInView';

const Coaching = () => {
  const {ref} = useSectionInView('Coaching', 0.5);

  return (
    <motion.section
      ref={ref}
      className="mb-28 max-w-[45rem] text-center leading-8 sm:mb-40 scroll-mt-28"
      initial={{opacity: 0, y: 100}}
      animate={{opacity: 1, y: 0}}
      transition={{delay: 0.175}}
      id="coaching">
      <SectionHeading>Coaching</SectionHeading>
      <ul className="mb-3">
        <li>
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Consequatur,
          necessitatibus?
        </li>
        <li>
          Quam ab excepturi sequi ipsam dolor, expedita aliquam quas fuga!
        </li>
        <li>
          Quae ea quaerat porro corrupti velit adipisci blanditiis eveniet sit!
        </li>
        <li>
          Laudantium dolor quibusdam quidem in! Eum sint obcaecati illo cum.
        </li>
        <li>
          Officia voluptates molestias, nihil dolore cum provident porro
          molestiae unde?
        </li>
        <li>
          Quidem corporis consequuntur culpa corrupti aliquam aperiam velit,
          sint possimus!
        </li>
        <li>
          Vitae inventore sit cupiditate dolorem voluptas aperiam soluta esse!
          Ipsam.
        </li>
        <li>
          Nam nihil, earum assumenda dolore sit deserunt mollitia rerum ullam.
        </li>
      </ul>
    </motion.section>
  );
};

export default Coaching;
