import {type User} from '../types/user';
import {client, TOKEN_KEY} from '../api';
import {useQuery} from '@tanstack/react-query';

client.interceptors.request.use(config => {
  const token = localStorage.getItem(TOKEN_KEY);
  if (token) {
    config.headers['Authorization'] = `Token ${token}`;
  }
  return config;
});

const getUserPerms = async () => {
  const response = await client.get<User>('/user/info/');
  return response.data;
};

export const useUserPerms = () =>
  useQuery({
    queryKey: ['user_perms'],
    queryFn: getUserPerms,
  });
