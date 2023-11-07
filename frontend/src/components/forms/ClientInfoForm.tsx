import {useForm} from 'react-hook-form';
import {ClientFormValues, ClientInfoSchema} from '../../types/clientInfo';
import {zodResolver} from '@hookform/resolvers/zod';
import {TOKEN_KEY} from '../../api';

const ClientInfoForm = () => {
  const {
    handleSubmit,
    formState: {errors},
    register,
  } = useForm<ClientFormValues>({
    resolver: zodResolver(ClientInfoSchema),
  });

  const token = localStorage.getItem(TOKEN_KEY);

  const onSubmit = (data: ClientFormValues) => {
    ClientInfoSchema.parse(data);
    console.log('data shape!!', data);

    fetch('http://127.0.0.1:8000/client/info/create/', {
      method: 'POST',
      headers: {
        Authorization: `Token ${token}`,
        'Content-Type': 'application/json',
      },
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
        console.log(data); // "Data inputted successfully!"
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
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
          className={`${
            errors.name && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.name && (
          <p className={'text-red-500 px-2'}>{errors.name?.message}</p>
        )}
        <input
          {...register('phone')}
          type="text"
          id="phone"
          placeholder="Phone Number"
          className={`${
            errors.phone && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.phone && (
          <p className={'text-red-500 px-2'}>{errors.phone?.message}</p>
        )}
        <input
          {...register('age')}
          type="text"
          id="age"
          placeholder="Age"
          className={`${errors.age && 'border-red-500 border rounded-md px-2'}`}
        />
        {errors.age && (
          <p className={'text-red-500 px-2'}>{errors.age?.message}</p>
        )}
        <input
          {...register('email')}
          type="email"
          id="email"
          placeholder="Email"
          className={`${
            errors.email && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.email && (
          <p className={'text-red-500 px-2'}>{errors.email?.message}</p>
        )}
        <input
          {...register('address')}
          type="text"
          id="address"
          placeholder="Address"
          className={`${
            errors.address && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.address && (
          <p className={'text-red-500 px-2'}>{errors.address?.message}</p>
        )}
        <input
          {...register('emergency_contact')}
          type="text"
          id="emergency-contact"
          placeholder="Emergency Contact"
          className={`${
            errors.emergency_contact && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.emergency_contact && (
          <p className={'text-red-500 px-2'}>
            {errors.emergency_contact?.message}
          </p>
        )}
        <input
          {...register('emergency_phone')}
          type="text"
          id="emergency-phone"
          placeholder="Emegency Contact Phone Number"
          className={`${
            errors.emergency_phone && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.emergency_phone && (
          <p className={'text-red-500 px-2'}>
            {errors.emergency_phone?.message}
          </p>
        )}
        <input
          {...register('height')}
          type="text"
          id="height"
          placeholder="Height"
          className={`${
            errors.height && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.height && (
          <p className={'text-red-500 px-2'}>{errors.height?.message}</p>
        )}
        <input
          {...register('weight')}
          type="text"
          id="weight"
          placeholder="Weight"
          className={`${
            errors.weight && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.weight && (
          <p className={'text-red-500 px-2'}>{errors.weight?.message}</p>
        )}
        <input
          {...register('ape_index')}
          type="text"
          id="ape-index"
          placeholder="Ape Index"
          className={`${
            errors.ape_index && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.ape_index && (
          <p className={'text-red-500 px-2'}>{errors.ape_index?.message}</p>
        )}
        <input
          {...register('occupation')}
          type="text"
          id="occupation"
          placeholder="Occupation"
          className={`${
            errors.occupation && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.occupation && (
          <p className={'text-red-500 px-2'}>{errors.occupation?.message}</p>
        )}
        <input
          {...register('hobbies')}
          type="text"
          id="hobbies"
          placeholder="Hobbies"
          className={`${
            errors.hobbies && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.hobbies && (
          <p className={'text-red-500 px-2'}>{errors.hobbies?.message}</p>
        )}

        <input
          {...register('health_concerns')}
          type="text"
          id="health-concerns"
          placeholder="Health Concerns"
          className={`${
            errors.health_concerns && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.health_concerns && (
          <p className={'text-red-500 px-2'}>
            {errors.health_concerns?.message}
          </p>
        )}
        <textarea
          {...register('primary_goals')}
          id="primary-goals"
          placeholder="Primary Goals"
          className={`${
            errors.primary_goals && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.primary_goals && (
          <p className={'text-red-500 px-2'}>{errors.primary_goals?.message}</p>
        )}
        <label htmlFor="parq-complete">
          Check if you have completed PAR-Q Form
        </label>
        <input
          {...register('parq_complete')}
          type="checkbox"
          id="parq-complete"
          className={`${
            errors.parq_complete && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.parq_complete && (
          <p className={'text-red-500 px-2'}>{errors.parq_complete?.message}</p>
        )}
        <label htmlFor="parq-complete">
          Check if you have completed Liability Waiver
        </label>
        <input
          {...register('liablitiy_waiver')}
          type="checkbox"
          id="liability-waiver"
          className={`${
            errors.liablitiy_waiver && 'border-red-500 border rounded-md px-2'
          }`}
        />
        {errors.liablitiy_waiver && (
          <p className={'text-red-500 px-2'}>
            {errors.liablitiy_waiver?.message}
          </p>
        )}
        <button type="submit" className="bg-red-200 rounded-md w-1/3">
          Submit Info
        </button>
      </form>
    </div>
  );
};

export default ClientInfoForm;
