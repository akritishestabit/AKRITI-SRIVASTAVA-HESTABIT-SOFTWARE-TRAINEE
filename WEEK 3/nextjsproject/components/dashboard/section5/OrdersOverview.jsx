import { orders } from "./data";
import OrderItem from "./OrderItem";

export default function OrdersOverview() {
  return (
    <div className="bg-white rounded-xl p-6 shadow-sm h-full">
      
      {/* HEADER */}
      <div className="mb-6">
        <h3 className="text-sm font-semibold text-gray-800">
          Orders overview
        </h3>
        <p className="text-xs text-green-500 mt-1">
          +30% this month
        </p>
      </div>

      {/* LIST */}
      <div className="space-y-4">
        {orders.map((order, index) => (
          <OrderItem key={index} order={order} />
        ))}
      </div>
    </div>
  );
}
