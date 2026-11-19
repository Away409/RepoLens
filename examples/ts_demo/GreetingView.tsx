import { message, type Greeting } from "./greeting";

export function GreetingView({ name }: Greeting) {
  return <h1>{message(name)}</h1>;
}
