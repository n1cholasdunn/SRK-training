import {useMutation} from '@tanstack/react-query';
import {client} from '../api';
import {z} from 'zod';
const submitAssessment = async <T>(
  url: string,
  data: T,
  validationSchema: z.ZodSchema<T>
) => {
  // Validate the data first
  validationSchema.parse(data);

  // Setup the Authorization header

  // Perform the POST request with axios
  const response = await client.post(url, data);
  return response.data;
};

// The hook itself
export const useSubmitAssessment = <T>(
  url: string,
  validationSchema: z.ZodSchema<T>
) => {
  // You could get the token from local storage, context, or Redux store as per your app's architecture
  // or however you manage your auth tokens

  // Use React Query's useMutation for the mutation
  return useMutation({
    // The mutation function
    mutationFn: (data: T) => submitAssessment(url, data, validationSchema),
    // Add any onSuccess, onError, etc. handlers here if needed
    onSuccess: data => {
      console.log('Data submitted successfully!', data);
    },
    onError: error => {
      console.error('There was an error!', error);
    },
  });
};
