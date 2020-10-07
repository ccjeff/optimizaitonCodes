A = [1 1 1 0 0;
    0 0 0 1 1;
    1 0 1 0 1;
    1 1 1 1 0;
    0 1 0 1 1];
PI = [0.8; 0.3; 0.40; 0.7; 0.6];
Q = [8; 5; 7; 8; 5];

cvx_begin
variables x(5,1) y
    maximize y
        subject to
            for i = 1:5
                y <= sum((A(:,i)).*x) - sum(PI.*x);
            end
            x <= Q;
            x >= 0;
cvx_end

x
y
