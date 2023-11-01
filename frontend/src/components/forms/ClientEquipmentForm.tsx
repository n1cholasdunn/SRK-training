import {zodResolver} from '@hookform/resolvers/zod';
import {useFieldArray, useForm} from 'react-hook-form';
import {EquipmentFormData, EquipmentFormSchema} from '../../types/equipment';

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

  const onSubmit = (data: EquipmentFormData) => {
    try {
      EquipmentFormSchema.parse(data);
      console.log(data);

      // TODO add submit logic
    } catch (error) {
      // TODO add error handling
    }
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
