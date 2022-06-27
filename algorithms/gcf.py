function gcf(x, y) {
  if (x == y) 
    return x;
  if (x > y) {
    if (x % y == 0)
      return y;
    return gcf(x % y, y);
  }
  if (y % x == 0)
    return x;
  return gcf(x, y % x);
}
