A = [-1 1 0;
    0 1 0;
    1 1 0;
    1 0 0;
    1 -1 0;
    -1 -1 0;
    -1 0 1;
    -1 1 sqrt(2); 
    0 1 1;
    1 1 sqrt(2);
    1 0 1;
    1 -1 sqrt(2);    
    0 -1 1;
    -1 -1 sqrt(2)];
b = [6;10;18;11;7;-1;0;6;10;18;11;7;0;-1];
cvx_begin
    variables x(3,1)
        maximize x(3)
            subject to 
                A * x <= b;
		x >= 0;
                      
cvx_end
x
