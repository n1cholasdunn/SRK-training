import {zodResolver} from '@hookform/resolvers/zod';
import {useFieldArray, useForm} from 'react-hook-form';
import {EquipmentFormData, EquipmentFormSchema} from '../../types/equipment';
import {TOKEN_KEY} from '../../api';

const ClientEquipmentForm = () => {
  const {
    handleSubmit,
    control,
    register,
    formState: {errors},
  } = useForm<EquipmentFormData>({
    resolver: zodResolver(EquipmentFormSchema),
    defaultValues: {
      equipment: [{name: ''}],
    },
  });

  const {fields, append, remove} = useFieldArray({
    control,
    name: 'equipment',
  });

  const token = localStorage.getItem(TOKEN_KEY);

  const onSubmit = (data: EquipmentFormData) => {
    EquipmentFormSchema.parse(data);
    console.log(data);
    fetch('http://127.0.0.1:8000/client/equipment/', {
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
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        {fields.map((field, index) => (
          <div key={field.id}>
            <input
              {...register(`equipment.${index}.name` as const)}
              defaultValue={field.name}
              placeholder="Type of equipment"
            />

            {errors.equipment && errors.equipment[index]?.name && (
              <p className="text-red-500">
                {errors.equipment[index]?.name?.message}
              </p>
            )}

            <button type="button" onClick={() => remove(index)}>
              Remove
            </button>
          </div>
        ))}

        <button type="button" onClick={() => append({name: ''})}>
          Add Equipment
        </button>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default ClientEquipmentForm;
