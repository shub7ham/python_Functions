def describe_attrs(cls):
  for attr,value in cls.__dict__.items():
    if not attr.startswith('__'):
      print(f'{attr} -> {value}')