import { render, screen } from '@testing-library/react';
import App from './App';

test('renders Best Bus header', () => {
  render(<App />);
  const linkElement = screen.getByText(/Best Bus/i);
  expect(linkElement).toBeInTheDocument();
});
