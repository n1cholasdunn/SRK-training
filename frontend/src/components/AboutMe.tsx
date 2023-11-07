import {motion} from 'framer-motion';
import SectionHeading from './ui/SectionHeading';
import {useSectionInView} from '../hooks/useSectionInView';

const AboutMe = () => {
  const {ref} = useSectionInView('About');

  return (
    <motion.section
      ref={ref}
      className="mb-28 max-w-[45rem] text-center leading-8 sm:mb-40 scroll-mt-28"
      initial={{opacity: 0, y: 100}}
      animate={{opacity: 1, y: 0}}
      transition={{delay: 0.175}}
      id="about">
      <SectionHeading>About Me</SectionHeading>
      <p className="mb-3">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Inventore
        dolorem cumque ratione perspiciatis amet neque vero explicabo
        repellendus perferendis officiis iure, doloribus alias sapiente et
        necessitatibus? Vero numquam sed sint, atque eligendi ab tempora
        assumenda voluptatem veritatis nam quasi. Saepe, maxime sunt amet facere
        iure odit rerum, quisquam totam animi inventore nesciunt vel, molestias
        laudantium. Ab, nulla odit blanditiis veritatis hic esse. Aliquam libero
        sunt qui quo eius, vel aspernatur! Nisi laudantium blanditiis aperiam
        temporibus doloremque dolores commodi libero. Consequuntur delectus
        possimus, ab animi quaerat quasi id placeat pariatur dolor ipsum,
        deleniti nisi corporis suscipit in deserunt vero! Placeat eos pariatur
        dolorum quia! Veniam architecto fugiat et porro aut quam perferendis
        doloremque assumenda animi voluptate laudantium sunt molestias
        aspernatur totam, repellat soluta ratione iure minus? Autem optio ad
        cupiditate iusto nesciunt tenetur facilis beatae quisquam mollitia
        commodi sequi blanditiis, libero qui officiis quia fugit quos explicabo
        fuga! Eaque, atque praesentium nulla odio iusto amet possimus libero
        tempore vel laudantium repellendus repudiandae provident maxime soluta
        qui expedita! Incidunt placeat quam nemo consequatur officia minus
        commodi impedit ab repudiandae molestias accusantium laboriosam saepe
        dolores fuga, tenetur sed quod praesentium expedita distinctio quisquam
        minima. Est, sint! Dignissimos iste nam eligendi, porro voluptatum
        molestiae!
      </p>
    </motion.section>
  );
};

export default AboutMe;
