import {useForm} from 'react-hook-form';
import {ClientFormValues, ClientInfoSchema} from '../../types/clientInfo';
import {zodResolver} from '@hookform/resolvers/zod';

const ClientInfoForm = () => {
  const {
    handleSubmit,
    formState: {errors},
    register,
  } = useForm<ClientFormValues>({
    resolver: zodResolver(ClientInfoSchema),
  });
  const onSubmit = (data: ClientFormValues) => {
    try {
      ClientInfoSchema.parse(data);
      console.log(data);

      // TODO add submit logic
    } catch (error) {
      // TODO add error handling
    }
  };
  return (
    <div className="my-6">
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex flex-col space-y-3">
        <input
          {...register('name')}
          type="text"
          id="name"
          placeholder="Name"
          className={`${errors.name && 'border-red-500'}`}
        />
        {errors.name && <p>{errors.name?.message}</p>}
        <input
          {...register('phone')}
          type="text"
          id="phone"
          placeholder="Phone Number"
          className={`${errors.phone && 'border-red-500'}`}
        />
        {errors.phone && <p>{errors.phone?.message}</p>}
        <input
          {...register('age')}
          type="text"
          id="age"
          placeholder="Age"
          className={`${errors.age && 'border-red-500'}`}
        />
        {errors.age && <p>{errors.age?.message}</p>}
        <input
          {...register('email')}
          type="email"
          id="email"
          placeholder="Email"
          className={`${errors.email && 'border-red-500'}`}
        />
        {errors.email && <p>{errors.email?.message}</p>}
        <input
          {...register('address')}
          type="text"
          id="address"
          placeholder="Address"
          className={`${errors.address && 'border-red-500'}`}
        />
        {errors.address && <p>{errors.address?.message}</p>}
        <input
          {...register('emergency_contact')}
          type="text"
          id="emergency-contact"
          placeholder="Emergency Contact"
          className={`${errors.emergency_contact && 'border-red-500'}`}
        />
        {errors.emergency_contact && <p>{errors.emergency_contact?.message}</p>}
        <input
          {...register('emergency_phone')}
          type="text"
          id="emergency-phone"
          placeholder="Emegency Contact Phone Number"
          className={`${errors.emergency_phone && 'border-red-500'}`}
        />
        {errors.emergency_phone && <p>{errors.emergency_phone?.message}</p>}
        <input
          {...register('height')}
          type="text"
          id="height"
          placeholder="Height"
          className={`${errors.height && 'border-red-500'}`}
        />
        {errors.height && <p>{errors.height?.message}</p>}
        <input
          {...register('weight')}
          type="text"
          id="weight"
          placeholder="Weight"
          className={`${errors.weight && 'border-red-500'}`}
        />
        {errors.weight && <p>{errors.weight?.message}</p>}
        <input
          {...register('ape_index')}
          type="text"
          id="ape-index"
          placeholder="Ape Index"
          className={`${errors.ape_index && 'border-red-500'}`}
        />
        {errors.ape_index && <p>{errors.ape_index?.message}</p>}
        <input
          {...register('occupation')}
          type="text"
          id="occupation"
          placeholder="Occupation"
          className={`${errors.occupation && 'border-red-500'}`}
        />
        {errors.occupation && <p>{errors.occupation?.message}</p>}
        <input
          {...register('hobbies')}
          type="text"
          id="hobbies"
          placeholder="Hobbies"
          className={`${errors.hobbies && 'border-red-500'}`}
        />
        {errors.hobbies && <p>{errors.hobbies?.message}</p>}
        <input
          {...register('primary_goals')}
          type="text"
          id="primary-goals"
          placeholder="Primary Goals"
          className={`${errors.primary_goals && 'border-red-500'}`}
        />
        {errors.primary_goals && <p>{errors.primary_goals?.message}</p>}
        <input
          {...register('health_concerns')}
          type="text"
          id="health-concerns"
          placeholder="Health Concerns"
          className={`${errors.health_concerns && 'border-red-500'}`}
        />
        {errors.health_concerns && <p>{errors.health_concerns?.message}</p>}
        <label htmlFor="parq-complete">
          Check if you have completed PAR-Q Form
        </label>
        <input
          {...register('parq_complete')}
          type="checkbox"
          id="parq-complete"
          className={`${errors.parq_complete && 'border-red-500'}`}
        />
        {errors.parq_complete && <p>{errors.parq_complete?.message}</p>}
        <label htmlFor="parq-complete">
          Check if you have completed Liability Waiver
        </label>
        <input
          {...register('liablitiy_waiver')}
          type="checkbox"
          id="liability-waiver"
          className={`${errors.liablitiy_waiver && 'border-red-500'}`}
        />
        {errors.liablitiy_waiver && <p>{errors.liablitiy_waiver?.message}</p>}
        <button type="submit" className="bg-red-200 rounded-md w-1/3">
          Submit
        </button>
      </form>
    </div>
  );
};

export default ClientInfoForm;
