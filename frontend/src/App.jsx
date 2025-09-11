import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './layout';
import Home from './pages/Home';
import Services from './pages/Services';
import Settings from './pages/Settings';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="/services" element={<Services />} />
          <Route path="/settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}