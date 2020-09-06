const sol = (a, b) => {
  let one, two;
  if (a > b) {
    two = a;
    one = b;
  } else {
    two = b;
    one = a;
  }
  let sum = 0;
  while (one <= two) {
    console.log(sum, one);
    sum += one;
    one++;
  }
  console.log(sum);
};

sol(3, 1);
