import { Link, Outlet, useLocation } from 'react-router-dom';
import { Home, Settings, CreditCard, Mic } from 'lucide-react';

const nav = [
  { path: '/', label: 'होम', icon: Home },
  { path: '/services', label: 'सेवाएं', icon: CreditCard },
  { path: '/settings', label: 'सेटिंग्स', icon: Settings },
];

export default function Layout() {
  const loc = useLocation();
  return (
    <div className="flex h-screen bg-gradient-to-br from-orange-50 via-white to-green-50">
      {/* Sidebar */}
      <aside className="w-64 bg-white shadow-lg p-4 space-y-4">
        <div className="flex items-center gap-2 text-xl font-bold">
          <Mic className="w-7 h-7 text-orange-600" /> BharatVaani
        </div>
        <nav className="space-y-2">
          {nav.map((n) => {
            const Icon = n.icon;
            return (
              <Link
                key={n.path}
                to={n.path}
                className={`flex items-center gap-3 px-3 py-2 rounded-lg transition-colors ${
                  loc.pathname === n.path
                    ? 'bg-orange-100 text-orange-700'
                    : 'hover:bg-orange-50'
                }`}
              >
                <Icon className="w-5 h-5" />
                <span className="hindi-font">{n.label}</span>
              </Link>
            );
          })}
        </nav>
      </aside>

      {/* Main */}
      <main className="flex-1 overflow-auto">
        <Outlet />
      </main>
    </div>
  );
}