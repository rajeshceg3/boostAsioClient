import { render, screen } from '@testing-library/react';
import App from './App';
import axios from 'axios';
jest.mock('axios', () => ({ get: jest.fn() }));
afterEach(() => jest.restoreAllMocks());
test('loads the actual backend message', async () => {
  axios.get.mockResolvedValueOnce({ data: { message: 'Hello from C++ backend!' } });
  render(<App />);
  expect(screen.getByText('Loading...')).toBeInTheDocument();
  expect(await screen.findByText('Hello from C++ backend!')).toBeInTheDocument();
  expect(axios.get).toHaveBeenCalledWith('http://localhost:8080/api/greet');
});
test('shows backend failure', async () => {
  jest.spyOn(console, 'error').mockImplementation(() => {});
  axios.get.mockRejectedValueOnce(new Error('offline'));
  render(<App />);
  expect(await screen.findByText('Failed to load message from backend.')).toBeInTheDocument();
});
