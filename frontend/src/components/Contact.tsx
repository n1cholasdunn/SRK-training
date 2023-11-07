import {motion} from 'framer-motion';
import {useSectionInView} from '../hooks/useSectionInView';
import SectionHeading from './ui/SectionHeading';
import toast from 'react-hot-toast';
import SubmitBtn from './SubmitBtn';
import {zodResolver} from '@hookform/resolvers/zod';
import {ContactFormSchema, ContactFormValues} from '../types/contactForm';
import {useForm} from 'react-hook-form';
import {Toaster} from 'react-hot-toast';

const Contact = () => {
  const {ref} = useSectionInView('Contact');
  const {
    handleSubmit,
    formState: {errors},
    register,
  } = useForm<ContactFormValues>({
    resolver: zodResolver(ContactFormSchema),
  });

  const onSubmit = (data: ContactFormValues) => {
    ContactFormSchema.parse(data);
    fetch('http://127.0.0.1:8000/contact/submit/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data),
    })
      .then(response => {
        if (response.ok) {
          console.log(response.json(), 'RESPONSE');
        } else {
          throw new Error('Server returned non-OK status: ' + response.status);
        }
      })
      .then(data => {
        console.log(data, 'hi toast');
        toast.success('Email sent successfully!');
      })
      .catch(error => {
        toast.error(error);
      });
  };

  return (
    <motion.section
      id="contact"
      ref={ref}
      className="mb-20 sm:mb-28 w-[min(100%,38rem)] text-center"
      initial={{
        opacity: 0,
      }}
      whileInView={{
        opacity: 1,
      }}
      transition={{
        duration: 1,
      }}
      viewport={{
        once: true,
      }}>
      <SectionHeading>Contact me</SectionHeading>

      <p className="text-gray-700 -mt-6 ">
        Please contact me directly at{' '}
        <a className="underline" href="mailto:sierra.rose.knott@gmail.com">
          sierra.rose.knott@gmail.com
        </a>{' '}
        or through this form.
      </p>

      <form
        onSubmit={handleSubmit(onSubmit)}
        className="mt-10 flex flex-col dark:text-black">
        <input
          {...register('sender_email')}
          className="h-14 px-4 rounded-lg borderBlack"
          placeholder="Your email"
        />
        {errors?.sender_email && (
          <p className={'text-red-500 text-2xl px-2'}>
            {errors?.sender_email?.message}
          </p>
        )}
        <textarea
          {...register('message')}
          className="h-52 my-3 rounded-lg borderBlack p-4"
          placeholder="Your message"
        />
        {errors?.message && (
          <p className={'text-red-500 text-2xl px-2'}>
            {errors?.message?.message}
          </p>
        )}
        <SubmitBtn />
        <Toaster />
      </form>
    </motion.section>
  );
};

export default Contact;
