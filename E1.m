function circle(x,y,r)
%x and y are the coordinates of the center of the circle
%r is the radius of the circle
%0.01 is the angle step, bigger values will draw the circle faster but
%you might notice imperfections (not very smooth)
ang=0:0.01:2*pi; 
xp=r*cos(ang);
yp=r*sin(ang);
plot(x+xp,y+yp, LineWidth=1.5, DisplayName = 'pos', Color='red');
end

x_data = importdata('x_collected.txt', '\t');
y_data = importdata('y_collected.txt');
phi_data = importdata('phi_collected.txt');

x = x_data;
y = y_data;
phi = phi_data;

[Ex,Ey] = gradient(phi, x, y);

Ex = Ex * -1;
Ey = Ey * -1;

surf(x, y, phi);
zlabel('$\varphi, [V]$', 'Interpreter','latex')
xlabel('$X$', 'Interpreter','latex')
ylabel('$Y$', 'Interpreter','latex')
colorbar
legend('rozkład potencjału w badanym polu')

figure
contour(x,y, phi)
hold on
quiver(x,y,Ex,Ey)
circle(5,8.5,3.75);
min_electrod = line([26 26], [4.5 11.5]);
min_electrod.Color = 'black';
min_electrod.LineWidth = 1.5;
xlabel('$X$', 'Interpreter','latex')
ylabel('$Y$', 'Interpreter','latex')
hold off
legend('linie ekwipotencjalne','wektory natężenia pola elektrycznego', 'katoda (cylindr)', 'anoda (płyta)')