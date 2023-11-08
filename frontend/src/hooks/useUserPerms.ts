import {type User} from '../types/user';
import {client} from '../api';
import {useQuery} from '@tanstack/react-query';

const getUserPerms = async () => {
  const response = await client.get<User>('/user/info/');
  return response.data;
};

export const useUserPerms = () =>
  useQuery({
    queryKey: ['user_perms'],
    queryFn: getUserPerms,
  });
