import { render, screen } from '@testing-library/react';
import Header from '../components/Header';

test('renders header text', () => {
  render(<Header />);
  expect(screen.getByText('My App')).toBeInTheDocument();
});
