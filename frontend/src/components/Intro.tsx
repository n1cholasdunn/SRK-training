import {motion} from 'framer-motion';
import {BsArrowRight, BsInstagram, BsYoutube} from 'react-icons/bs';
import {useSectionInView} from '../hooks/useSectionInView';
import {useActiveSectionContext} from '../hooks/useActiveSectionContext';
const Intro = () => {
  const {ref} = useSectionInView('Home');
  const {setActiveSection, setTimeOfPrevClick} = useActiveSectionContext();

  return (
    <section
      ref={ref}
      id="home"
      className="mb-28 max-w-[50rem] text-center sm:mb-0 scroll-mt-[100rem]">
      <div className="flex items-center justify-center">
        <div className="relative pt-4">
          <motion.div
            initial={{opacity: 0, scale: 0}}
            animate={{opacity: 1, scale: 1}}
            transition={{
              type: 'tween',
              duration: 0.2,
            }}>
            <img
              src="src/assets/introPhoto.jpg"
              alt="Sierra portrait"
              width="250"
              height="250"
              className="h-30 w-30  rounded-full object-cover border-[0.35rem] border-white shadow-xl"
            />
          </motion.div>

          <motion.span
            className="absolute bottom-0 right-0 text-6xl"
            initial={{opacity: 0, scale: 0}}
            animate={{opacity: 1, scale: 1}}
            transition={{
              type: 'spring',
              stiffness: 125,
              delay: 0.1,
              duration: 0.7,
            }}>
            🧗🏻‍♀️
          </motion.span>
        </div>
      </div>

      <motion.h1
        className="mb-10 mt-4 px-4 text-2xl font-medium !leading-[1.5] sm:text-4xl"
        initial={{opacity: 0, y: 100}}
        animate={{opacity: 1, y: 0}}>
        <span className="font-medium">
          Hello I am Sierra a Rock Climbing Coach. Lorem ipsum dolor sit amet
          consectetur adipisicing elit. Quisquam repellendus quod deleniti
          aperiam animi reprehenderit tempore corporis amet in! Unde?
        </span>
        .
      </motion.h1>

      <motion.div
        className="flex flex-col sm:flex-row items-center justify-center gap-2 px-4 text-lg font-medium"
        initial={{opacity: 0, y: 100}}
        animate={{opacity: 1, y: 0}}
        transition={{
          delay: 0.1,
        }}>
        <a
          href="#contact"
          className="group bg-gray-900 text-white px-7 py-3 flex items-center gap-2 rounded-full outline-none focus:scale-110 hover:scale-110 hover:bg-gray-950 active:scale-105 transition"
          onClick={() => {
            setActiveSection('Contact');
            setTimeOfPrevClick(Date.now());
          }}>
          Contact me here{' '}
          <BsArrowRight className="opacity-70 group-hover:translate-x-1 transition" />
        </a>

        <a
          className="bg-white p-4 text-gray-700 hover:text-gray-950 flex items-center gap-2 rounded-full focus:scale-[1.15] hover:scale-[1.15] active:scale-105 transition cursor-pointer borderBlack"
          href="https://instagram.com/sierraroseknott"
          target="_blank">
          <BsInstagram />
        </a>

        <a
          className="bg-white p-4 text-gray-700 flex items-center gap-2 text-[1.35rem] rounded-full focus:scale-[1.15] hover:scale-[1.15] hover:text-gray-950 active:scale-105 transition cursor-pointer borderBlack"
          href="https://youtube.com/@SierraRoseKnott?si=UYJz0Ecv3DpL5e3m"
          target="_blank">
          <BsYoutube />
        </a>
      </motion.div>
    </section>
  );
};

export default Intro;
